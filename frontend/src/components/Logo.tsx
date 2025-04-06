import React from 'react';
import { Box } from '@mui/material';

const Logo: React.FC = () => {
    return (
        <Box sx={{ 
            display: 'flex', 
            alignItems: 'center',
            gap: 1
        }}>
            <Box sx={{
                width: 40,
                height: 40,
                borderRadius: '50%',
                background: 'linear-gradient(135deg, #4a6bff 0%, #1a4bff 100%)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                boxShadow: '0 4px 12px rgba(74, 107, 255, 0.2)',
                position: 'relative',
                overflow: 'hidden',
                '&::before': {
                    content: '""',
                    position: 'absolute',
                    width: '100%',
                    height: '100%',
                    background: 'linear-gradient(45deg, transparent 0%, rgba(255,255,255,0.1) 50%, transparent 100%)',
                    animation: 'shine 3s infinite',
                },
                '@keyframes shine': {
                    '0%': { transform: 'translateX(-100%)' },
                    '100%': { transform: 'translateX(100%)' }
                }
            }}>
                <Box component="span" sx={{
                    color: 'white',
                    fontWeight: 'bold',
                    fontSize: '1.5rem',
                    textShadow: '0 2px 4px rgba(0,0,0,0.1)'
                }}>
                    H
                </Box>
            </Box>
            <Box sx={{
                fontSize: '1.5rem',
                fontWeight: 'bold',
                background: 'linear-gradient(135deg, #4a6bff 0%, #1a4bff 100%)',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
                letterSpacing: '0.5px'
            }}>
                Heimdrw
            </Box>
        </Box>
    );
};

export default Logo; 