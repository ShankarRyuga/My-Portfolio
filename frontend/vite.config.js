import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  base: '/My-Portfolio/',
  build: {
    outDir: '../dist'
  }
})
