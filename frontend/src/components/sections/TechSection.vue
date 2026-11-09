<!-- src/components/sections/TechSection.vue -->
<script setup lang="ts">
const abilities = [
  { number: '01', title: '研发设计', detail: '企业资料记载拥有两大研发中心，持续开展学生书包设计与产品迭代。' },
  { number: '02', title: '生产制造', detail: '资料记载拥有 10 条生产线、150 余台生产设备，形成从原料加工到成品制造的能力。' },
  { number: '03', title: '质量检测', detail: '设置检测实验室，对拉链、振荡等项目开展产品测试。' }
]
function hideBrokenImage(event: Event) { (event.target as HTMLImageElement).style.display = 'none' }
</script>

<template>
  <section id="strength" class="section-pad bg-brand-navy text-white"><div class="container-site"><div class="reveal grid gap-8 lg:grid-cols-2 lg:items-end"><div><p class="section-kicker !text-red-300">03 / OUR STRENGTH</p><div class="eyebrow-line"></div><h2 class="text-3xl font-black leading-tight md:text-5xl">从设计到制造，<br />让品质有迹可循</h2></div><p class="max-w-xl text-base leading-8 text-slate-300 md:text-lg">研发、生产与检测环环相扣，是亿鸿持续打磨儿童书包的重要基础。</p></div><div class="mt-14 grid gap-5 lg:grid-cols-3"><article v-for="item in abilities" :key="item.number" class="reveal rounded-2xl border border-white/15 bg-white/5 p-7 backdrop-blur-sm"><p class="text-sm font-bold text-red-300">{{ item.number }} / CAPABILITY</p><h3 class="mt-10 text-2xl font-black">{{ item.title }}</h3><p class="mt-4 text-sm leading-7 text-slate-300">{{ item.detail }}</p></article></div><div class="reveal relative mt-6 min-h-[280px] overflow-hidden rounded-2xl bg-slate-800 md:min-h-[420px]"><div class="absolute inset-0 bg-gradient-to-r from-slate-800 to-slate-700"></div><img :src="'/images/factory-2.jpg'" alt="亿鸿皮具生产车间" class="absolute inset-0 h-full w-full object-cover opacity-70" loading="lazy" @error="hideBrokenImage" /><div class="absolute inset-0 bg-gradient-to-r from-brand-navy/90 to-transparent"></div><div class="absolute bottom-8 left-8 max-w-lg md:bottom-12 md:left-12"><p class="text-xs tracking-[.25em] text-red-300">MANUFACTURING & QUALITY</p><p class="mt-3 text-2xl font-bold md:text-4xl">每一道工序，都关乎使用体验</p></div></div></div></section>
</template>
