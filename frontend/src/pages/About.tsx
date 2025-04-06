import React from 'react';
import { Box, Typography, Paper } from '@mui/material';

const About: React.FC = () => {
  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        About Financial Audit App
      </Typography>
      <Paper elevation={3} sx={{ p: 4, mt: 2 }}>
        <Typography variant="body1" paragraph>
          The Financial Audit App is a powerful tool designed to help businesses and organizations
          streamline their financial audit processes. Our application allows you to upload XML files
          containing financial data, which are then processed and analyzed for audit purposes.
        </Typography>
        <Typography variant="body1" paragraph>
          Key features:
        </Typography>
        <ul>
          <li>Secure XML file upload and processing</li>
          <li>Automated financial data analysis</li>
          <li>Comprehensive audit reporting</li>
          <li>User-friendly interface</li>
        </ul>
      </Paper>
    </Box>
  );
};

export default About; 