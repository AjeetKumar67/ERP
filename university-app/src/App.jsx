import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Home from './components/Home';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import CollegeList from './components/College/CollegeList';
import CollegeDetail from './components/College/CollegeDetail';
import Dashboard from './components/Dashboard'; // Import Dashboard component

const App = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    const handleLogin = () => {
        setIsLoggedIn(true);
    };

    return (
        <Router>
            {isLoggedIn && <Header />}
            <Routes>
                <Route path="/login" element={<Login onLogin={handleLogin} />} />
                <Route path="/register" element={<Register />} />
                <Route path="/colleges/:id" element={<CollegeDetail />} />
                <Route path="/colleges" element={<CollegeList />} />
                <Route path="/home" element={<Home />} />

                <Route path="/" element={isLoggedIn ? <Dashboard /> : <Home />} />
            </Routes>
        </Router>
    );
};

export default App;
