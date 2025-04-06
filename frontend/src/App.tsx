import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider, CssBaseline } from '@mui/material';
import { theme } from './theme';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';
import { AppBar, Toolbar, Button, Box, Typography } from '@mui/material';
import { useNavigate, useLocation } from 'react-router-dom';
import HomeIcon from '@mui/icons-material/Home';
import InfoIcon from '@mui/icons-material/Info';
import ContactMailIcon from '@mui/icons-material/ContactMail';
import Logo from './components/Logo';

const App: React.FC = () => {
    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <Router>
                <Box sx={{ flexGrow: 1 }}>
                    <AppBar position="static" elevation={0} sx={{ 
                        backgroundColor: 'transparent',
                        backdropFilter: 'blur(8px)',
                        borderBottom: '1px solid rgba(255, 255, 255, 0.1)'
                    }}>
                        <Toolbar sx={{ 
                            display: 'flex',
                            justifyContent: 'space-between',
                            alignItems: 'center',
                            px: 3
                        }}>
                            {/* Logo and Navigation */}
                            <Box sx={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                                <Logo />
                                <Box sx={{ display: 'flex', gap: 3 }}>
                                    <Button
                                        onClick={() => window.location.href = '/'}
                                        sx={{
                                            color: window.location.pathname === '/' ? 'primary.main' : 'text.primary',
                                            textTransform: 'none',
                                            fontWeight: window.location.pathname === '/' ? 'bold' : 'normal',
                                            fontSize: '1.1rem',
                                            letterSpacing: '0.5px',
                                            '&:hover': {
                                                backgroundColor: 'transparent',
                                                color: 'primary.main',
                                            }
                                        }}
                                    >
                                        Home
                                    </Button>
                                    <Button
                                        onClick={() => window.location.href = '/about'}
                                        sx={{
                                            color: window.location.pathname === '/about' ? 'primary.main' : 'text.primary',
                                            textTransform: 'none',
                                            fontWeight: window.location.pathname === '/about' ? 'bold' : 'normal',
                                            fontSize: '1.1rem',
                                            letterSpacing: '0.5px',
                                            '&:hover': {
                                                backgroundColor: 'transparent',
                                                color: 'primary.main',
                                            }
                                        }}
                                    >
                                        About
                                    </Button>
                                    <Button
                                        onClick={() => window.location.href = '/contact'}
                                        sx={{
                                            color: window.location.pathname === '/contact' ? 'primary.main' : 'text.primary',
                                            textTransform: 'none',
                                            fontWeight: window.location.pathname === '/contact' ? 'bold' : 'normal',
                                            fontSize: '1.1rem',
                                            letterSpacing: '0.5px',
                                            '&:hover': {
                                                backgroundColor: 'transparent',
                                                color: 'primary.main',
                                            }
                                        }}
                                    >
                                        Contact
                                    </Button>
                                </Box>
                            </Box>
                        </Toolbar>
                    </AppBar>
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/about" element={<About />} />
                        <Route path="/contact" element={<Contact />} />
                    </Routes>
                </Box>
            </Router>
        </ThemeProvider>
    );
};

export default App;
