<template>
    <div class="min-h-screen flex flex-col ">
        <nav class="bg-white shadow-md w-full h-24">
      <div class=" mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-full">
          <div class="flex items-center h-full">
            <img src="/public/logo.png" alt="Logo" class="w-16 mt-4">
          </div>
        </div>
      </div>
    </nav>
  
  
      <div class="flex flex-col md:flex-row items-center justify-center">
          <form class="bg-white border-4 border-purple w-56 mt-32 md:w-96 py-12 px-16 md:px-8 rounded-lg shadow-md text-left" @submit.prevent="login">
            <label class="mt-2 ml-1 block tracking-wide text-lg text-black mb-1 md:mb-5">Email:</label>
            <input type="email" id="email" class="shadow-md w-full h-12 px-5 py-2 border-2 border-purple rounded-lg text-lg mb-5" v-model="user_data.email" required>
            
            <label class="mt-5 ml-1 block tracking-wide text-lg text-black mb-1 md:mb-5">Password:</label>
            <input type="password" class="shadow-md w-full h-12 px-5 py-2 border-2 border-purple rounded-lg text-lg mb-5"  v-model="user_data.password" required>
            
            <button class="bg-gradient-to-r from-purple to-peach hover:from-lightblue hover:to-grey rounded-lg px-4 py-2 ml-16 my-10 md:my-10 md:w-48 text-white text-lg mx-auto" type="submit">Sign-in</button>
            
            <p class="text-base text-center text-black">
              Don't have an account? <router-link to="/signup" class="text-blue-500 hover:underline">Sign up</router-link>
            </p>
          </form>
        </div>
    </div>

  </template>
  
  
<script setup>
import { ref } from 'vue'; 
import { useRouter } from 'vue-router'; 
import axios from 'axios';
import { useToast } from "vue-toastification";
 const toast = useToast({ position: 'bottom-right' });


const router = useRouter();
const user_data=ref({
  email:'',
  password:'',
})

const login = () => {
    axios.post('http://127.0.0.1:8000/token/', {
        email: user_data.value.email, 
        password: user_data.value.password})
        .then(response => {
      const { access, refresh, user_type, user_id, user_email } = response.data;
      localStorage.setItem('accessToken', access);
      localStorage.setItem('refreshToken', refresh);
      localStorage.setItem('userType', user_type);
      localStorage.setItem('userId', user_id);
      localStorage.setItem('userEmail', user_email);
      console.log('Logged in');
      if (user_type === 'admin') {
        router.push({ name: 'Allartist' });
      } else if (user_type === 'artist') {
        router.push({ name: 'Artistpro' });
      } else {
        console.error('No user',error.message)
      }
    })
    .catch(error => {
      console.error('Login failed:', error.message);
    });
  };
</script>