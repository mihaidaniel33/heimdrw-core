import React from 'react';
import { Box } from '@mui/material';

const CurvedBackground: React.FC = () => {
    return (
        <Box sx={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            height: '100%',
            overflow: 'hidden',
            zIndex: -1,
            '&::before': {
                content: '""',
                position: 'absolute',
                top: 0,
                left: 0,
                right: 0,
                height: '100%',
                background: 'linear-gradient(135deg, rgba(74, 107, 255, 0.1) 0%, rgba(26, 75, 255, 0.05) 100%)',
                clipPath: 'polygon(0 0, 100% 0, 100% 85%, 0 100%)',
            },
            '&::after': {
                content: '""',
                position: 'absolute',
                top: 0,
                left: 0,
                right: 0,
                height: '100%',
                background: 'linear-gradient(135deg, rgba(74, 107, 255, 0.05) 0%, rgba(26, 75, 255, 0.02) 100%)',
                clipPath: 'polygon(0 0, 100% 0, 100% 70%, 0 85%)',
                animation: 'wave 8s ease-in-out infinite',
            },
            '@keyframes wave': {
                '0%': { transform: 'translateY(0) rotate(0deg)' },
                '50%': { transform: 'translateY(-10px) rotate(1deg)' },
                '100%': { transform: 'translateY(0) rotate(0deg)' }
            }
        }}>
            {/* Decorative circles */}
            <Box sx={{
                position: 'absolute',
                top: '20%',
                right: '10%',
                width: 200,
                height: 200,
                borderRadius: '50%',
                background: 'radial-gradient(circle, rgba(74, 107, 255, 0.1) 0%, rgba(74, 107, 255, 0) 70%)',
                animation: 'pulse 4s ease-in-out infinite',
            }} />
            <Box sx={{
                position: 'absolute',
                top: '40%',
                left: '5%',
                width: 150,
                height: 150,
                borderRadius: '50%',
                background: 'radial-gradient(circle, rgba(74, 107, 255, 0.1) 0%, rgba(74, 107, 255, 0) 70%)',
                animation: 'pulse 6s ease-in-out infinite',
            }} />
            <Box sx={{
                position: 'absolute',
                bottom: '10%',
                right: '20%',
                width: 100,
                height: 100,
                borderRadius: '50%',
                background: 'radial-gradient(circle, rgba(74, 107, 255, 0.1) 0%, rgba(74, 107, 255, 0) 70%)',
                animation: 'pulse 5s ease-in-out infinite',
            }} />
            <style>
                {`
                    @keyframes pulse {
                        0% { transform: scale(1); opacity: 0.5; }
                        50% { transform: scale(1.2); opacity: 0.3; }
                        100% { transform: scale(1); opacity: 0.5; }
                    }
                `}
            </style>
        </Box>
    );
};

export default CurvedBackground; 