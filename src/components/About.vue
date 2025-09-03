<template>
  <div class="container">
    <section class="about-me">
      <h2 class="section-header">About Me</h2>
      <div class="about-content">
        <div class="profile-photo">
          <img src="/Shankar.jpeg" alt="Your Name's Profile Photo" class="photo" />
        </div>
        <p>Hello! My name is [Your Name]. I am a passionate [Your Title] with a strong focus on [Your Niche]. I love building clean and efficient applications and I am always eager to learn new technologies. I believe in continuous learning and enjoy exploring new challenges.</p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'AboutPage',
};
</script>

<style scoped>
.about-me {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.about-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

.section-header {
  background-color: #b4c0cc;
  color: #333;
  padding: 0.8rem 2rem;
  border-radius: 8px;
  width: 100%;
  text-align: center;
  margin-bottom: 2rem;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}

.profile-photo {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  overflow: hidden;
  border: 4px solid #007bff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

p {
  max-width: 700px;
  line-height: 1.8;
  font-size: 1.1rem;
}

@media (min-width: 768px) {
  .about-content {
    flex-direction: row;
    text-align: left;
  }
}
</style>