import React, { useState } from 'react';
import { Box, Button, Typography, Paper, Alert, CircularProgress } from '@mui/material';
import { Upload as UploadIcon } from '@mui/icons-material';
import axios from 'axios';

const Home: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [message, setMessage] = useState<{ type: 'success' | 'error', text: string } | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      setFile(event.target.files[0]);
      setMessage(null);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage({ type: 'error', text: 'Please select a file first' });
      return;
    }

    setIsLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8000/api/v1/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        responseType: 'blob',
      });

      // Create a URL for the blob
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      
      // Get filename from Content-Disposition header or use a default
      const contentDisposition = response.headers['content-disposition'];
      let filename = 'processed_data.xlsx';
      if (contentDisposition) {
        const filenameMatch = contentDisposition.match(/filename=(.+)/);
        if (filenameMatch && filenameMatch[1]) {
          filename = filenameMatch[1];
        }
      }
      
      link.setAttribute('download', filename);
      document.body.appendChild(link);
      link.click();
      link.remove();
      
      setMessage({ type: 'success', text: 'File processed and downloaded successfully!' });
      setFile(null);
    } catch (error) {
      setMessage({ type: 'error', text: 'Error processing file. Please try again.' });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        Financial Audit Upload
      </Typography>
      <Paper elevation={3} sx={{ p: 4, mt: 2 }}>
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
          <input
            accept=".xml"
            style={{ display: 'none' }}
            id="raised-button-file"
            type="file"
            onChange={handleFileChange}
          />
          <label htmlFor="raised-button-file">
            <Button
              variant="contained"
              component="span"
              startIcon={<UploadIcon />}
              disabled={isLoading}
            >
              Select XML File
            </Button>
          </label>
          {file && (
            <Typography variant="body1">
              Selected file: {file.name}
            </Typography>
          )}
          <Box sx={{ position: 'relative' }}>
            <Button
              variant="contained"
              color="primary"
              onClick={handleUpload}
              disabled={!file || isLoading}
            >
              Process and Download Excel
            </Button>
            {isLoading && (
              <CircularProgress
                size={24}
                sx={{
                  position: 'absolute',
                  top: '50%',
                  left: '50%',
                  marginTop: '-12px',
                  marginLeft: '-12px',
                }}
              />
            )}
          </Box>
        </Box>
        {message && (
          <Alert severity={message.type} sx={{ mt: 2 }}>
            {message.text}
          </Alert>
        )}
      </Paper>
    </Box>
  );
};

export default Home; 