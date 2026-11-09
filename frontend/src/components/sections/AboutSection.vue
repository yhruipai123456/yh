<!-- src/components/sections/AboutSection.vue -->
<script setup lang="ts">
const stats = [
  { value: '2005', unit: '年', label: '公司成立' },
  { value: '2', unit: '大', label: '研发中心' },
  { value: '10', unit: '条', label: '生产线' },
  { value: '80', unit: '万', label: '资料所载年产量（个包）' }
]
function hideBrokenImage(event: Event) { (event.target as HTMLImageElement).style.display = 'none' }
</script>

<template>
  <section id="about" class="section-pad bg-white">
    <div class="container-site grid gap-12 lg:grid-cols-2 lg:items-center lg:gap-20">
      <div class="reveal relative min-h-[400px] overflow-hidden rounded-[2rem] bg-slate-100 md:min-h-[540px]"><div class="absolute inset-0 bg-gradient-to-br from-slate-200 via-slate-100 to-red-50"></div><img :src="'/images/factory-1.jpg'" alt="亿鸿皮具生产基地" class="absolute inset-0 h-full w-full object-cover" loading="lazy" @error="hideBrokenImage" /><div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-brand-navy/85 to-transparent p-8 text-white"><p class="text-xs tracking-[.25em]">ABOUT YIHONG</p><p class="mt-2 text-2xl font-bold">以匠心，做好每一个书包</p></div></div>
      <div class="reveal"><p class="section-kicker">01 / ABOUT US</p><div class="eyebrow-line"></div><h2 class="section-title">专注儿童书包<br /><span class="text-brand-red">持续探索成长所需</span></h2><p class="section-copy mt-7">广州市亿鸿皮具有限公司于 2005 年在广州花都狮岭创立，集儿童书包研发、生产和销售于一体。公司以“健康、时尚、安全、减负”为理念，持续打磨书包的设计与使用体验。</p><p class="section-copy mt-4">瑞牌 RUIPAI 聚焦学生书包，以产品研发、制造与品质管理，回应孩子和家长对日常背负体验的期待。</p><a href="#history" class="mt-7 inline-flex items-center gap-2 font-bold text-brand-red hover:gap-4">了解发展历程 <span aria-hidden="true">→</span></a></div>
    </div>
    <div class="container-site mt-16"><div class="reveal grid grid-cols-2 gap-px overflow-hidden rounded-2xl bg-slate-200 md:grid-cols-4"><div v-for="item in stats" :key="item.label" class="bg-slate-50 p-6 md:p-9"><p class="text-4xl font-black text-brand-navy md:text-5xl">{{ item.value }}<span class="ml-1 text-base text-brand-red">{{ item.unit }}</span></p><p class="mt-3 text-sm text-slate-500">{{ item.label }}</p></div></div></div>
  </section>
</template>
