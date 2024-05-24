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
        <form v-if="artist"  @submit.prevent="updateArtist"class="bg-white border-2 border-green-600 w-4/12 h-2/3 ml-1/2 mt-10 px-10 py-8  mr-20 text-left shadow-md rounded-lg">
          <div>
              <div>
                  <label class="block text-lg font-medium text-black mb-1">ID</label>
                  <input type="number" name="blogId"class="shadow-md w-full h-10 px-5 py-2 border-2 border-gray-300 rounded-lg text-lg mb-5" v-model="artist.id"disabled>
              </div>
              <div>
                  <label class="block text-lg font-medium text-black mb-1">First Name</label>
                  <input type="text" name="title"class="shadow-md w-full h-10 px-5 py-2 border-2 border-gray-300 rounded-lg text-lg mb-5" v-model="artist.first_name">
              </div>
              <div>
                  <label class="block text-lg font-medium text-black mb-1">Last Name</label>
                  <input type="text" name="title"class="shadow-md w-full h-10 px-5 py-2 border-2 border-gray-300 rounded-lg text-lg mb-5" v-model="artist.last_name">
              </div>
              <div>
                  <label for="" class="block text-lg font-medium text-black mb-1">Email</label>
                  <textarea name="description" class="shadow-md w-full h-10 px-5 py-2 border-2 border-gray-300 rounded-lg text-lg mb-5" v-model="artist.email"></textarea>
              </div>
              <div>
                  <label for="" class="block text-lg font-medium text-black mb-1">DOB</label>
                  <textarea name="description" class="shadow-md w-full h-10 px-5 py-2 border-2 border-gray-300 rounded-lg text-lg mb-5" v-model="artist.dob"></textarea>
              </div>
              <div>
                  <label for="" class="block text-lg font-medium text-black mb-1">Country</label>
                  <textarea name="description" class="shadow-md w-full h-10 px-5 py-2 border-2 border-gray-300 rounded-lg text-lg mb-5" v-model="artist.country"></textarea>
              </div>
              <div>
                  <label for="" class="block text-lg font-medium text-black mb-1">Bio</label>
                  <textarea name="description" class="shadow-md w-full h-20 px-5 py-2 border-2 border-gray-300 rounded-lg text-lg mb-5" v-model="artist.bio"></textarea>
              </div>
              <div>
                <label class="block text-lg text-gray-700 mb-2">Gender</label>
                <select v-model="artist.gender" class="w-full px-4 py-2 mb-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500 text-lg">
                    <option value="M">Male</option>
                    <option value="F">Female</option>
                    <option value="O">Others</option>
                </select>
            </div>
              <div class="flex justify-evenly">
                  <button class="rounded-lg ring-2 ring-lime-500 py-2 px-5 mt-6">Update</button>
                  <button class="rounded-lg ring-2 ring-red-500 py-2 px-5 mt-6" @click="cancelUpdate">Cancel</button>
              </div>
          </div>
      </form>
        </div>
    </div>

  </template>
<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const router = useRouter();
const artistId = ref(route.params.artistId);
const artist = ref(null);

const fetchArtist = () => {
    const accessToken = localStorage.getItem('accessToken');
    axios.get(`http://127.0.0.1:8000/user/${artistId.value}/`, {
        headers: {
          Authorization: `Bearer ${accessToken}`
        }
      })
      .then(response => {
        const artistData = response.data;
        artist.value = artistData;
      })
      .catch(error => {
        console.error(error);
      });
  };
  
  const updateArtist = (id) => {
    const accessToken = localStorage.getItem('accessToken');
    axios.patch(`http://127.0.0.1:8000/user/${artistId.value}/`, {
        first_name: artist.value.first_name,
        last_name: artist.value.last_name,
        email: artist.value.email,
        dob: artist.value.dob,
        gender: artist.value.gender,
        country: artist.value.country,
        bio: artist.value.bio,
      }, {
        headers: {
          Authorization: `Bearer ${accessToken}`
        }
      })
      .then(response => {
        console.log('Artist Updated', response.data);
        router.push({ name: 'Artistpro' });
      })
      .catch(error => {
        console.error(error);
      });
  };
  
  const cancelUpdate = () => {
    router.push({ name: 'Artistpro' });
  };
  
  onMounted(fetchArtist);
</script>
