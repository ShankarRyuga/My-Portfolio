<template>
  <div id="app">
    <div class="background-video-container">
      <video autoplay muted loop class="background-video">
        <source src="/video.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
    <Header />
    <main class="main-content-container">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
import Header from './components/Header.vue';

export default {
  name: 'App',
  components: {
    Header,
  },
};
</script>

<style>
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f0f2f5;
  color: #333;
}

#app {
  position: relative;
  min-height: 100vh;
}

.background-video-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: -1;
}

.background-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  background-color: rgba(0, 0, 0, 0.4); 
}

.main-content-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 1rem;
}

.container {
  background-color: #fff;
  padding: 2.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  margin: 2rem 0;
}

h2 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 2rem;
  font-weight: 600;
  font-size: 2.5rem;
}

button {
  padding: 0.8rem 1.5rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

button:hover {
  background-color: #0056b3;
  transform: translateY(-2px);
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
  transform: translateY(0);
}

@media (max-width: 768px) {
  .container {
    padding: 1.5rem;
    margin: 1rem 0;
  }
}
</style>