<template>
    <div class="min-h-screen bg-gray-100 flex flex-col">
     <nav class="bg-white shadow-md shawdow-purple w-full h-24">
       <div class=" mx-auto px-4 sm:px-6 lg:px-8">
         <div class="flex items-center justify-between h-full">
           <div class="flex items-center h-full">
             <img src="/public/logo.png" alt="Logo" class="w-16 mt-4">
           </div>
         </div>
       </div>
     </nav>
 
     <div class="flex flex-col md:flex-row items-center justify-around">
       <form class="bg-white border-2 border-lightblue w-6/12 h-4/5 mt-8 px-10 py-8 text-left shadow-md rounded-lg" @submit.prevent="addUser">
         <div class="grid grid-cols-2 gap-5">
           <div>
             <label class="block text-lg font-medium text-black mb-1">First Name:</label>
             <input type="text" name="fname" id="fname" class="shadow-md w-full h-10 px-5 py-2 border-2 border-blue rounded-lg text-lg mb-5" v-model="user.first_name" required>
           </div>
           <div>
             <label class="block text-lg font-medium text-black mb-1">Last Name:</label>
             <input type="text" name="lname" id="lname" class="shadow-md w-full h-10 px-5 py-2 border-2 border-blue rounded-lg text-lg mb-5" v-model="user.last_name" required>
           </div>
           <div>
             <label class="block text-lg font-medium text-black mb-1">Email:</label>
             <input type="email" name="email" id="email" class="shadow-md w-full h-10 px-5 py-2 border-2 border-blue rounded-lg text-lg mb-5" v-model="user.email" required>
           </div>
           <div>
             <label class="block text-lg font-medium text-black mb-1">Password:</label>
             <input type="password" name="password" id="password" class="shadow-md w-full h-10 px-5 py-2 border-2 border-blue rounded-lg text-lg mb-5" v-model="user.password" required>
           </div>
           <div>
             <label class="block text-lg font-medium text-black mb-1">Confirm Password:</label>
             <input type="password" name="confpassword" id="cpassword" class="shadow-md w-full h-10 px-5 py-2 border-2 border-blue rounded-lg text-lg mb-5" v-model="user.confirmPassword" required>
           </div>
           <div>
             <label class="block text-lg font-medium text-black mb-1">Date of Birth:</label>
             <input type="date" name="dob" id="dob" class="shadow-md w-full h-10 px-5 py-2 border-2 border-blue rounded-lg text-lg mb-5" v-model="user.dob" required>
           </div>
           <div>
             <label class="block text-lg font-medium text-black mb-1">Bio</label>
             <textarea name="bio" id="bio" class="shadow-md w-full h-32 px-5 py-2 border-2 border-blue rounded-lg text-lg mb-5" v-model="user.bio"></textarea>
           </div>
           <div>
           <label class="block text-lg font-medium text-black mb-1">Gender:</label>
           <select name="gender" id="gender" class="shadow-md w-full h-10 px-5 py-2 border-2 border-blue rounded-lg text-lg mb-5" v-model="user.gender">
             <option value="">Select Gender</option>
             <option value="M">Male</option>
             <option value="F">Female</option>
             <option value="O">Other</option>
           </select>
         </div>
         <div>
           <label class="block text-lg font-medium text-black mb-1">Country:</label>
           <input type="text" name="country" id="country" class="shadow-md w-full h-10 px-5 py-2 border-2 border-blue rounded-lg text-lg mb-5"v-model="user.country">
         </div>
         </div>
         <div class="flex justify-center">
           <button type="submit" class="ring-2 ring-purple rounded-lg px-4 py-2 text-black mr-12 mt-6">Sign-up</button>
           <button @click="cancelSign" type="button" class="ring-2 ring-pink rounded-lg px-4 py-2 text-black mt-6">Cancel</button>
         </div>
       </form>
     </div>
   </div>
 </template>
 <script setup>
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  import { ref } from 'vue';
  import { useToast } from "vue-toastification";
  const toast = useToast({ position: 'bottom-left' });
 
  const user = ref({
      email: '',
      password: '',
      first_name: '',
      last_name: '',
      dob:'',
      bio: '',
      gender: '',
      country: '',
      user_type: 'artist',
  });
  
  const router = useRouter();
 
  const addUser = () => {
    const accessToken = localStorage.getItem('accessToken');
    if (!accessToken) {
        console.error('No access token found');
        return;
    }

    axios.post('http://127.0.0.1:8000/register/', {
        email: user.value.email,
        password: user.value.password,
        first_name: user.value.first_name,
        last_name: user.value.last_name,
        dob: user.value.dob,
        bio: user.value.bio,
        gender: user.value.gender,
        country: user.value.country,
        user_type: user.value.user_type
    }, {
        headers: {
            Authorization: `Bearer ${accessToken}`
        }
    })
    .then(response => {
        console.log("added artist")
        router.push({ name: 'Allartist' });
        toast.success("artist added ")
    })
    .catch(error => {
        console.error(error);
        toast.success("unsuccessful")
    });
};

  const cancelSign=()=>{
   router.push({name:'Allartist'})
  }
  </script>
  
 