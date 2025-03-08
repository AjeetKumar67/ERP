import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Import Routes
import Header from './components/Header';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import CollegeList from './components/College/CollegeList';
import CollegeDetail from './components/College/CollegeDetail';
import Main from './components/Main'; // Import Main component

const App = () => {
    return (
        <Router>
            <Header />
            <Routes> {/* Use Routes instead of Switch */}
                <Route path="/login" element={<Login />} /> {/* Use element prop */}
                <Route path="/register" element={<Register />} />
                <Route path="/colleges/:id" element={<CollegeDetail />} />
                <Route path="/colleges" element={<CollegeList />} />
                <Route path="/" element={<Main />} /> {/* Set Main as the default route */}
            </Routes>
        </Router>
    );
};

export default App;
