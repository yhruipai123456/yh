<!-- src/views/HomeView.vue -->
<script setup lang="ts">
import { onBeforeUnmount, onMounted } from 'vue'
import AppHeader from '../components/layout/AppHeader.vue'
import AppFooter from '../components/layout/AppFooter.vue'
import HeroSection from '../components/sections/HeroSection.vue'
import AboutSection from '../components/sections/AboutSection.vue'
import HistorySection from '../components/sections/HistorySection.vue'
import TechSection from '../components/sections/TechSection.vue'
import ProductsSection from '../components/sections/ProductsSection.vue'
import NewsSection from '../components/sections/NewsSection.vue'
import PartnersSection from '../components/sections/PartnersSection.vue'

let observer: IntersectionObserver | undefined
onMounted(() => {
  const targets = document.querySelectorAll<HTMLElement>('.reveal')
  if (!('IntersectionObserver' in window)) {
    targets.forEach((item) => item.classList.add('is-visible'))
    return
  }
  observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible')
        observer?.unobserve(entry.target)
      }
    })
  }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' })
  targets.forEach((item) => observer?.observe(item))
})
onBeforeUnmount(() => observer?.disconnect())
</script>

<template>
  <a href="#main" class="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[100] focus:bg-white focus:p-3">跳转到主要内容</a>
  <AppHeader />
  <main id="main">
    <HeroSection />
    <AboutSection />
    <HistorySection />
    <TechSection />
    <ProductsSection />
    <NewsSection />
    <PartnersSection />
  </main>
  <AppFooter />
</template>