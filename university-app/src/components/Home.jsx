import React from 'react';
import { Container, Typography, Button, Grid, Card, CardContent, CardActions } from '@mui/material';
import { Link } from 'react-router-dom';
import './Home.css'; // Import the CSS file for additional styling

const Home = () => {
    return (
        <Container className="home" maxWidth="lg">
            <Typography variant="h2" component="h1" gutterBottom>
                Welcome to the School Site
            </Typography>
            <Typography variant="body1" gutterBottom>
                Please log in to access more features.
            </Typography>
            <Button variant="contained" color="primary" component={Link} to="/login">
                Login
            </Button>

            <Grid container spacing={4} className="features">
                <Grid item xs={12} sm={6} md={4}>
                    <Card>
                        <CardContent>
                            <Typography variant="h5" component="h2">
                                Feature 1
                            </Typography>
                            <Typography variant="body2" component="p">
                                Description of feature 1.
                            </Typography>
                        </CardContent>
                        <CardActions>
                            <Button size="small" color="primary" component={Link} to="/feature1">
                                Learn More
                            </Button>
                        </CardActions>
                    </Card>
                </Grid>
                <Grid item xs={12} sm={6} md={4}>
                    <Card>
                        <CardContent>
                            <Typography variant="h5" component="h2">
                                Feature 2
                            </Typography>
                            <Typography variant="body2" component="p">
                                Description of feature 2.
                            </Typography>
                        </CardContent>
                        <CardActions>
                            <Button size="small" color="primary" component={Link} to="/feature2">
                                Learn More
                            </Button>
                        </CardActions>
                    </Card>
                </Grid>
                <Grid item xs={12} sm={6} md={4}>
                    <Card>
                        <CardContent>
                            <Typography variant="h5" component="h2">
                                Feature 3
                            </Typography>
                            <Typography variant="body2" component="p">
                                Description of feature 3.
                            </Typography>
                        </CardContent>
                        <CardActions>
                            <Button size="small" color="primary" component={Link} to="/feature3">
                                Learn More
                            </Button>
                        </CardActions>
                    </Card>
                </Grid>
            </Grid>
        </Container>
    );
};

export default Home;
