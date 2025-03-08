import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import collegeService from '../../services/collegeService';

const CollegeDetail = () => {
    const { id } = useParams();
    const [college, setCollege] = useState(null);

    useEffect(() => {
        const fetchCollege = async () => {
            const response = await collegeService.getCollege(id);
            setCollege(response.data);
        };
        fetchCollege();
    }, [id]);

    if (!college) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h2>{college.name}</h2>
            <p>{college.address}</p>
            <p>Established: {college.established_date}</p>
        </div>
    );
};

export default CollegeDetail;
