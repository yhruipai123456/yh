<!-- src/components/sections/HeroSection.vue -->
<script setup lang="ts">
const highlights = ['专注儿童书包', '研发 · 生产 · 销售', '健康 · 时尚 · 安全 · 减负']
function hideBrokenImage(event: Event) { (event.target as HTMLImageElement).style.display = 'none' }
</script>

<template>
  <section id="home" class="relative isolate flex min-h-[650px] items-center overflow-hidden bg-brand-navy py-24 text-white md:min-h-[720px]">
    <div class="absolute inset-0 bg-gradient-to-br from-[#192b4b] via-brand-navy to-[#050b18]"></div>
    <img :src="'/images/hero-bg.jpg'" alt="瑞牌学生书包品牌形象" class="absolute inset-0 h-full w-full object-cover opacity-35" @error="hideBrokenImage" />
    <div class="absolute inset-0 bg-gradient-to-r from-brand-navy via-brand-navy/90 to-transparent"></div>
    <div class="container-site relative z-10 grid gap-10 lg:grid-cols-2 lg:items-center">
      <div class="reveal max-w-2xl">
        <p class="mb-5 text-xs font-bold uppercase tracking-[.35em] text-red-300 md:text-sm">YIHONG LEATHER GOODS · RUIPAI</p>
        <h1 class="text-5xl font-black leading-[1.15] tracking-tight md:text-7xl">新护脊<span class="text-brand-red">·</span><br />选瑞牌</h1>
        <p class="mt-7 max-w-xl text-lg leading-8 text-slate-200 md:text-xl">从新减负，新护未来。亿鸿皮具专注儿童书包，以设计、制造与品质，陪伴孩子轻松成长。</p>
        <div class="mt-9 flex flex-wrap gap-4"><a href="#products" class="btn-primary">探索产品系列 <span class="ml-2">↗</span></a><a href="#about" class="btn-outline">了解亿鸿</a></div>
        <div class="mt-12 flex flex-wrap gap-x-6 gap-y-3 border-t border-white/20 pt-6 text-xs tracking-wide text-slate-300"><span v-for="item in highlights" :key="item">{{ item }}</span></div>
      </div>
      <div class="relative hidden min-h-[430px] lg:block" aria-hidden="true"><div class="absolute right-0 top-5 h-80 w-80 rounded-full border border-white/15"></div><div class="absolute right-12 top-16 h-64 w-64 rounded-full border border-white/15"></div><div class="absolute bottom-0 right-5 text-[160px] font-black leading-none tracking-tighter text-white/[.06]">R</div><p class="absolute bottom-12 right-0 border-l-4 border-brand-red pl-5 text-right text-sm font-semibold leading-7 text-white/80">NEW BACKPACK<br />NEW JOURNEY</p></div>
    </div>
    <a href="#about" class="absolute bottom-8 left-1/2 z-10 -translate-x-1/2 text-xs tracking-[.3em] text-white/70">SCROLL ↓</a>
  </section>
</template>
