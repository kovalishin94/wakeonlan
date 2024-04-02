<template>
    <div class="h-[80vh] grid min-h-full place-items-center bg-white px-6 py-24 sm:py-32 lg:px-8">
        <div class="text-center">
            <p class="text-5xl font-semibold text-gray-600">404</p>
            <h1 class="mt-4 text-3xl font-bold tracking-tight text-gray-900 sm:text-5xl">
                Страница не найдена
            </h1>
            <RouterLink :to="{ name: 'wakeup' }" class="bg-gray-200 hover:bg-gray-400 px-5 py-3">На главную</RouterLink>
        </div>
    </div>
</template>
  