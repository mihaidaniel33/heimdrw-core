import React from 'react';
import { Box, Typography, Paper, TextField, Button } from '@mui/material';

const Contact: React.FC = () => {
  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        Contact Us
      </Typography>
      <Paper elevation={3} sx={{ p: 4, mt: 2 }}>
        <Box component="form" sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
          <TextField
            required
            id="name"
            label="Name"
            variant="outlined"
            fullWidth
          />
          <TextField
            required
            id="email"
            label="Email"
            type="email"
            variant="outlined"
            fullWidth
          />
          <TextField
            required
            id="message"
            label="Message"
            multiline
            rows={4}
            variant="outlined"
            fullWidth
          />
          <Button
            variant="contained"
            color="primary"
            type="submit"
            sx={{ alignSelf: 'flex-start' }}
          >
            Send Message
          </Button>
        </Box>
      </Paper>
    </Box>
  );
};

export default Contact; 