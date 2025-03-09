import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Header.css'; // Import the CSS file for styling

const Header = () => {
    const [dropdownOpen, setDropdownOpen] = useState(false);
    const [collegesDropdownOpen, setCollegesDropdownOpen] = useState(false);

    const toggleDropdown = () => {
        setDropdownOpen(!dropdownOpen);
    };

    const toggleCollegesDropdown = () => {
        setCollegesDropdownOpen(!collegesDropdownOpen);
    };

    const closeDropdowns = () => {
        setDropdownOpen(false);
        setCollegesDropdownOpen(false);
    };

    return (
        <header className="header">
            <div className="logo">
                <Link to="/">University App</Link>
            </div>
            <nav>
                <ul className="nav-links">
                    <li>
                        <Link to="/">Home</Link> {/* Update the link to navigate to the home route */}
                    </li>
                    <li>
                        <Link to="/login">Login</Link>
                    </li>
                    <li>
                        <Link to="/register">Register</Link>
                    </li>
                    <li className="dropdown">
                        <button onClick={toggleCollegesDropdown} className="dropdown-toggle">
                            Colleges
                        </button>
                        {collegesDropdownOpen && (
                            <ul className="dropdown-menu" onClick={closeDropdowns}>
                                <li>
                                    <Link to="/colleges">All Colleges</Link>
                                </li>
                                <li>
                                    <Link to="/colleges/add">Add College</Link>
                                </li>
                                <li>
                                    <Link to="/colleges/edit">Edit College</Link>
                                </li>
                                <li>
                                    <Link to="/colleges/delete">Delete College</Link>
                                </li>
                                {/* Add more college functionalities as needed */}
                            </ul>
                        )}
                    </li>
                    <li className="dropdown">
                        <button onClick={toggleDropdown} className="dropdown-toggle">
                            Components
                        </button>
                        {dropdownOpen && (
                            <ul className="dropdown-menu" onClick={closeDropdowns}>
                                <li>
                                    <Link to="/component1">Component 1</Link>
                                </li>
                                <li>
                                    <Link to="/component2">Component 2</Link>
                                </li>
                                <li>
                                    <Link to="/component3">Component 3</Link>
                                </li>
                                {/* Add more components as needed */}
                            </ul>
                        )}
                    </li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
