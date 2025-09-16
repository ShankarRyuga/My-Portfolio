<template>
  <div class="container">
    <section class="contact">
      <h2 class="section-header">Contact Me</h2>
      <form @submit.prevent="submitForm" class="contact-form">
        <div class="form-group">
          <label for="name">Name</label>
          <input type="text" id="name" v-model="form.name" required>
        </div>
        
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="form.email" required>
        </div>
        
        <div class="form-group">
          <label for="message">Message</label>
          <textarea id="message" v-model="form.message" rows="5" required></textarea>
        </div>
        
        <button type="submit" :disabled="isSubmitting">
          {{ isSubmitting ? 'Sending...' : 'Send' }}
        </button>

        <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </form>
    </section>
  </div>
</template>

<script>
export default {
  name: 'ContactPage',
  data() {
    return {
      form: {
        name: '',
        email: '',
        message: ''
      },
      isSubmitting: false,
      successMessage: '',
      errorMessage: ''
    };
  },
  methods: {
    async submitForm() {
      this.isSubmitting = true;
      this.successMessage = '';
      this.errorMessage = '';

      try {
        const response = await fetch('http://localhost:5000/send_email', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.form),
        });

        const result = await response.json();
        
        if (response.ok) {
          this.successMessage = result.message;
          this.form.name = '';
          this.form.email = '';
          this.form.message = '';
        } else {
          this.errorMessage = result.message || 'Something went wrong.';
        }
      } catch (error) {
        this.errorMessage = 'Failed to connect to the server.';
        console.error('Error submitting form:', error);
      } finally {
        this.isSubmitting = false;
      }
    }
  }
};
</script>

<style scoped>
.section-header {
  background-color: #b4c0cc;
  color: #333;
  padding: 0.8rem 2rem;
  border-radius: 8px;
  text-align: center;
  margin-bottom: 2rem;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 600px;
  margin: 0 auto;
}

.form-group {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 1rem;
  width: 100%;
}

.contact-form label {
  font-weight: bold;
  width: 100px;
  text-align: right;
}

.contact-form input,
.contact-form textarea {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.contact-form button {
  padding: 0.8rem 1.5rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
  width: 400px;
  margin: 0 auto;
}

.contact-form button:hover {
  background-color: #0056b3;
  transform: translateY(-2px);
}
</style>