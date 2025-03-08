import axios from 'axios';

const API_URL = 'http://localhost:8000/api/colleges/';

const getColleges = () => {
    return axios.get(API_URL);
};

const getCollege = (id) => {
    return axios.get(API_URL + id + '/');
};

const collegeService = {
    getColleges,
    getCollege,
};

export default collegeService;
