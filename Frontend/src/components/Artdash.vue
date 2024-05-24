<template>
    <div class="min-h-screen flex">
      <div class="flex">
        <nav class="bg-gray-800 w-64 min-h-screen flex flex-col text-white">
  
          <div class="flex flex-col flex-grow px-6 bg-blue items-center">
            <img src="/public/logo2.png" alt="Logo" class=" flex w-24 mt-5 mb-10 ">
            <router-link to="/artist-profile" class="text-white text-xl mb-5 hover:text-darkblue">My Profile</router-link>
            <router-link to="" class="text-white text-xl mb-5 hover:text-darkblue">Tracks</router-link>
            <button @click="logoutDash"class="text-white text-xl mb-5 hover:text-darkblue">Logout</button>
          </div>
        </nav>
      </div>
    </div>
  </template>
  
  <script setup>
  import{ useRouter } from 'vue-router';
const router=useRouter()
const logoutDash = async () => {
  try {
    
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    localStorage.removeItem('userId');
    localStorage.removeItem('username');
    router.push('/');
    console.log("logged out")
  } catch (error) {
    console.error('Logout error:', error.message);
  }
};
  </script>
  