import React, { useState } from 'react';
import { Box, Container, Typography, TextField, Button, Paper, CircularProgress, Alert } from '@mui/material';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import DescriptionIcon from '@mui/icons-material/Description';
import EmailIcon from '@mui/icons-material/Email';
import DownloadIcon from '@mui/icons-material/Download';
import axios from 'axios';

const Home: React.FC = () => {
    const [file, setFile] = useState<File | null>(null);
    const [email, setEmail] = useState<string>('');
    const [message, setMessage] = useState<{ type: 'success' | 'error' | 'info', text: string } | null>(null);
    const [isLoading, setIsLoading] = useState(false);
    const [processedData, setProcessedData] = useState<Blob | null>(null);
    const [filename, setFilename] = useState<string>('');

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files[0]) {
            const selectedFile = event.target.files[0];
            // Check if file is XML by extension or MIME type
            if (selectedFile.name.endsWith('.xml') || selectedFile.name.endsWith('.XML') || selectedFile.type === 'text/xml' || selectedFile.type === 'application/xml') {
                setFile(selectedFile);
                setMessage(null);
                setProcessedData(null); // Reset processed data when new file is selected
            } else {
                setMessage({ type: 'error', text: 'Please upload a valid XML file' });
                setFile(null);
            }
        }
    };

    const handleProcess = async () => {
        if (!file || !email) {
            setMessage({ type: 'error', text: 'Please select a file and enter your email' });
            return;
        }

        setIsLoading(true);
        setMessage({ type: 'info', text: 'Processing file...' });
        
        const formData = new FormData();
        formData.append('file', file);
        formData.append('email', email);

        try {
            const response = await fetch('http://localhost:8000/api/v1/upload', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const blob = await response.blob();
            if (blob.size === 0) {
                throw new Error('Received empty file');
            }

            setProcessedData(blob);
            setFilename(`saft_data_${email.split('@')[0]}.xlsx`);
            setMessage({ type: 'success', text: 'File processed successfully! Click Download to get your file.' });
        } catch (error) {
            console.error('Error processing file:', error);
            setMessage({ type: 'error', text: error instanceof Error ? error.message : 'Failed to process file' });
        } finally {
            setIsLoading(false);
        }
    };

    const handleDownload = () => {
        if (processedData) {
            const url = window.URL.createObjectURL(processedData);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
        }
    };

    return (
        <Container maxWidth="md">
            <Box sx={{ 
                minHeight: '100vh',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                py: 8,
                gap: 4
            }}>
                {/* Header Section */}
                <Box sx={{ textAlign: 'center', mb: 4 }}>
                    <Typography variant="h3" component="h1" gutterBottom sx={{ 
                        fontWeight: 'bold',
                        color: 'primary.main',
                        mb: 2
                    }}>
                        SAF-T Processor
                    </Typography>
                    <Typography variant="h6" color="text.secondary" sx={{ maxWidth: 600, mx: 'auto' }}>
                        Transform your SAF-T XML files into organized Excel spreadsheets with ease. 
                        Our tool helps you analyze and manage your financial data efficiently.
                    </Typography>
                </Box>

                {/* Form Section */}
                <Paper elevation={3} sx={{ 
                    p: 4, 
                    width: '100%',
                    maxWidth: 600,
                    borderRadius: 2,
                    backgroundColor: 'background.paper'
                }}>
                    <Box sx={{ display: 'flex', flexDirection: 'column', gap: 3 }}>
                        {/* Email Input */}
                        <TextField
                            fullWidth
                            label="Email Address"
                            variant="outlined"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            InputProps={{
                                startAdornment: <EmailIcon sx={{ color: 'action.active', mr: 1 }} />
                            }}
                        />

                        {/* File Upload */}
                        <Box sx={{ 
                            border: '2px dashed',
                            borderColor: 'primary.main',
                            borderRadius: 2,
                            p: 3,
                            textAlign: 'center',
                            cursor: 'pointer',
                            '&:hover': {
                                backgroundColor: 'action.hover',
                            }
                        }}>
                            <input
                                type="file"
                                accept=".xml"
                                onChange={handleFileChange}
                                style={{ display: 'none' }}
                                id="file-upload"
                            />
                            <label htmlFor="file-upload">
                                <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 1 }}>
                                    <CloudUploadIcon sx={{ fontSize: 48, color: 'primary.main' }} />
                                    <Typography variant="body1">
                                        {file ? file.name : 'Click to upload SAF-T XML file'}
                                    </Typography>
                                    <Typography variant="body2" color="text.secondary">
                                        Supported format: .xml
                                    </Typography>
                                </Box>
                            </label>
                        </Box>

                        {/* Process Button */}
                        <Button
                            variant="contained"
                            size="large"
                            onClick={handleProcess}
                            disabled={isLoading || !file || !email}
                            sx={{ 
                                py: 1.5,
                                borderRadius: 2,
                                textTransform: 'none',
                                fontSize: '1.1rem',
                                background: 'linear-gradient(45deg, #4a6bff 30%, #1a4bff 90%)',
                                transition: 'all 0.3s ease',
                                opacity: (!file || !email) ? 0.7 : 1,
                                '&:hover': {
                                    transform: 'translateY(-2px)',
                                    boxShadow: '0 4px 8px rgba(74, 107, 255, 0.2)',
                                },
                                '&:disabled': {
                                    background: 'linear-gradient(45deg, #4a6bff 30%, #1a4bff 90%)',
                                    opacity: 0.5,
                                }
                            }}
                        >
                            {isLoading ? (
                                <CircularProgress size={24} color="inherit" />
                            ) : (
                                'Upload'
                            )}
                        </Button>

                        {/* Download Button */}
                        {processedData && (
                            <Button
                                variant="contained"
                                size="large"
                                onClick={handleDownload}
                                startIcon={<DownloadIcon />}
                                sx={{ 
                                    py: 1.5,
                                    borderRadius: 2,
                                    textTransform: 'none',
                                    fontSize: '1.1rem',
                                    background: 'linear-gradient(45deg, #4CAF50 30%, #2E7D32 90%)',
                                    transition: 'all 0.3s ease',
                                    '&:hover': {
                                        transform: 'translateY(-2px)',
                                        boxShadow: '0 4px 8px rgba(76, 175, 80, 0.2)',
                                    }
                                }}
                            >
                                Download Processed File
                            </Button>
                        )}

                        {/* Message Display */}
                        {message && (
                            <Alert 
                                severity={message.type} 
                                sx={{ 
                                    mt: 2,
                                    '& .MuiAlert-icon': {
                                        alignItems: 'center'
                                    }
                                }}
                            >
                                {message.text}
                            </Alert>
                        )}
                    </Box>
                </Paper>

                {/* Features Section */}
                <Box sx={{ 
                    display: 'grid',
                    gridTemplateColumns: { xs: '1fr', md: 'repeat(3, 1fr)' },
                    gap: 3,
                    mt: 4,
                    width: '100%'
                }}>
                    {[
                        {
                            icon: <DescriptionIcon sx={{ fontSize: 40, color: 'primary.main' }} />,
                            title: 'Easy Processing',
                            description: 'Simply upload your SAF-T XML file and get instant results'
                        },
                        {
                            icon: <CloudUploadIcon sx={{ fontSize: 40, color: 'primary.main' }} />,
                            title: 'Secure Upload',
                            description: 'Your data is processed securely and never stored'
                        },
                        {
                            icon: <EmailIcon sx={{ fontSize: 40, color: 'primary.main' }} />,
                            title: 'Email Updates',
                            description: 'Receive notifications about your processed files'
                        }
                    ].map((feature, index) => (
                        <Paper key={index} elevation={2} sx={{ p: 3, textAlign: 'center', borderRadius: 2 }}>
                            {feature.icon}
                            <Typography variant="h6" sx={{ mt: 2, mb: 1 }}>
                                {feature.title}
                            </Typography>
                            <Typography variant="body2" color="text.secondary">
                                {feature.description}
                            </Typography>
                        </Paper>
                    ))}
                </Box>
            </Box>
        </Container>
    );
};

export default Home; 