import socket

from wakeonlan import send_magic_packet

from scapy.layers.l2 import getmacbyip

from pythonping import ping

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core import serializers, models


@api_view(['GET'])
def me(request):
    user_serializer = serializers.UserSerializer(request.user)
    return Response(user_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_my_pc(request):
    data = {
        'last_name': '',
        'first_name': '',
        'computername': '',
        'ip_address': '',
        'mac': '',
        'is_running': False,
    }
    data['last_name'] = request.user.last_name
    data['first_name'] = request.user.first_name
    data['computername'] = 'comp' + request.user.username.replace('.', '') + '.server.alter'
    try:
        data['ip_address'] = socket.gethostbyname(data.get('computername'))
    except:
        return Response({'info': data, 'message': 'Не удалось получить IP по DNS имени, обратитесь к системному администратору'}, status=status.HTTP_206_PARTIAL_CONTENT)
    
    ping_result = ping(data.get('ip_address'), count=2)

    if ping_result.stats_packets_returned > 0:
        data['is_running'] = True
        return Response({'info': data, 'message': 'ПК уже запущен'}, status=status.HTTP_200_OK)

    try:
        comp = models.Computer.objects.get(ip_address=data.get('ip_address'))
        data['mac'] = comp.mac_address
        for i in data.get('mac'):
            data['mac'] = data['mac'].replace(':', '-')
        return Response({'info': data}, status=status.HTTP_200_OK)               
    except:
        data['message'] = 'Нет мак-адреса в БД, обратитесь к системному администратору'
        return Response({'info': data}, status=status.HTTP_206_PARTIAL_CONTENT)


@api_view(['POST'])
def wake_up_computer(request):
    mac = request.data.get('mac')
    ip_address = request.data.get('ip_address')
    
    if not mac:
        try:
            comp = models.Computer.objects.get(ip_address=ip_address)
            mac = comp.mac_address
            if not mac:
                return Response({'message': 'Нет MAC адреса и не удалось получить его по IP, обратитесь к системному администратору'}, status=status.HTTP_400_BAD_REQUEST)
            for i in mac:
                mac = mac.replace(':', '-')
        except:
            return Response({'message': 'Нет MAC адреса и не удалось получить его по IP, обратитесь к системному администратору'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        send_magic_packet(mac, ip_address=ip_address)
    except:
        return Response({'message': 'Не получилось отправить пакет, обратитесь к системному администратору'}, status=status.HTTP_400_BAD_REQUEST)
    
    ping_result = ping(ip_address, timeout=5, count=10, interval=2)

    if ping_result.stats_packets_returned == 0:
        return Response({'message': 'Пакет отправлен но ПК не пингуется попробуйте ещё раз или обратитесь к системному администратору', 'is_running': False}, status=status.HTTP_200_OK)

    return Response({'message': 'ПК запущен', 'is_running': True}, status=status.HTTP_200_OK)
    
