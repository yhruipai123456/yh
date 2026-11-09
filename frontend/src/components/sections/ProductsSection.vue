<!-- src/components/sections/ProductsSection.vue -->
<script setup lang="ts">
const products = [
  { name: '轻尚游学系列', en: 'TRAVEL & STUDY', image: '/images/product-1.jpg', text: '轻快出发，陪伴每一次探索。' },
  { name: '美式学院系列', en: 'CAMPUS CLASSIC', image: '/images/product-2.jpg', text: '从容穿梭校园，表达年轻活力。' },
  { name: '新贵英伦系列', en: 'BRITISH STYLE', image: '/images/product-3.jpg', text: '经典轮廓，呈现别样校园气质。' },
  { name: '运动休闲系列', en: 'SPORT & LEISURE', image: '/images/product-4.jpg', text: '自由切换学习与运动的节奏。' },
  { name: '户外出走系列', en: 'OUTDOOR JOURNEY', image: '/images/product-5.jpg', text: '把好奇心装进背包，走向更广阔的世界。' }
]
function hideBrokenImage(event: Event) { (event.target as HTMLImageElement).style.display = 'none' }
</script>

<template>
  <section id="products" class="section-pad bg-white"><div class="container-site"><div class="reveal flex flex-col justify-between gap-6 md:flex-row md:items-end"><div><p class="section-kicker">04 / PRODUCT SERIES</p><div class="eyebrow-line"></div><h2 class="section-title">不同风格，<br />同样认真出发</h2></div><p class="max-w-md text-sm leading-7 text-slate-600 md:text-base">围绕学习、运动与出行场景，瑞牌打造多元学生书包系列。</p></div><div class="mt-14 grid gap-5 sm:grid-cols-2 lg:grid-cols-3"><article v-for="(product, index) in products" :key="product.name" class="reveal group overflow-hidden rounded-2xl border border-slate-100 bg-slate-50" :class="index === 0 ? 'lg:col-span-2' : ''"><div class="relative aspect-[4/3] overflow-hidden bg-gradient-to-br from-slate-200 via-white to-red-100" :class="index === 0 ? 'lg:aspect-[2/1]' : ''"><img :src="product.image" :alt="product.name + '书包产品展示'" class="h-full w-full object-cover transition duration-500 group-hover:scale-105" loading="lazy" @error="hideBrokenImage" /><span class="absolute left-5 top-5 rounded-full bg-white/90 px-3 py-1 text-[10px] font-bold tracking-widest text-brand-navy">{{ product.en }}</span></div><div class="p-6"><h3 class="text-xl font-black text-brand-navy">{{ product.name }}</h3><p class="mt-2 text-sm text-slate-600">{{ product.text }}</p></div></article></div><p class="mt-6 text-xs text-slate-500">系列名称依据企业简介；产品图以实际切图为准。</p></div></section>
</template>
