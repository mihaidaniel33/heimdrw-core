import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider, CssBaseline, AppBar, Toolbar, Container, Box } from '@mui/material';
import { theme } from './theme';
import Home from './pages/Home';
import Logo from './components/Logo';
import CurvedBackground from './components/CurvedBackground';

const App: React.FC = () => {
    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <Router>
                <Box sx={{ 
                    minHeight: '100vh',
                    position: 'relative',
                    background: 'linear-gradient(135deg, #f5f7ff 0%, #ffffff 100%)'
                }}>
                    <CurvedBackground />
                    <AppBar 
                        position="static" 
                        elevation={0}
                        sx={{ 
                            background: 'transparent',
                            backdropFilter: 'blur(10px)',
                            borderBottom: '1px solid rgba(74, 107, 255, 0.1)'
                        }}
                    >
                        <Toolbar>
                            <Container maxWidth="lg" sx={{ display: 'flex', alignItems: 'center' }}>
                                <Logo />
                                <Box sx={{ flexGrow: 1 }} />
                                {/* Add navigation items here if needed */}
                            </Container>
                        </Toolbar>
                    </AppBar>
                    <Routes>
                        <Route path="/" element={<Home />} />
                    </Routes>
                </Box>
            </Router>
        </ThemeProvider>
    );
};

export default App;
