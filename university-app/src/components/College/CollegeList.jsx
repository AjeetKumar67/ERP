import React, { useState, useEffect } from 'react';
import collegeService from '../../services/collegeService';

const CollegeList = () => {
    const [colleges, setColleges] = useState([]);

    useEffect(() => {
        const fetchColleges = async () => {
            const response = await collegeService.getColleges();
            setColleges(response.data);
        };
        fetchColleges();
    }, []);

    return (
        <div>
            <h2>Colleges</h2>
            {colleges.length === 0 ? (
                <p>No colleges available.</p>
            ) : (
                <ul>
                    {colleges.map(college => (
                        <li key={college.id}>{college.name}</li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default CollegeList;
