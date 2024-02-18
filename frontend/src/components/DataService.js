import axios from 'axios';

const apiClient = axios.create({
    baseURL:'http://localhost:5000/api',
    headers: {
        Accept:'application/json',
        'Content-Type':'application/json',

    },
});

const getData = async (timeRange) => {
    try{
        const response = await apiClient.get(`/data?timeRange=${timeRange}`);
        return response.data;
    }catch(error){
        throw error;
    }
};

export default {
    getData,
};
