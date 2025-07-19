// API Configuration
export const API_CONFIG = {
  // Default API base URL - can be overridden by environment variables
  BASE_URL: import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000',
  
  // API endpoints
  ENDPOINTS: {
    ANALYZE_RESUME: '/analyze-resume/',
  }
}

// Helper function to get full API URL
export const getApiUrl = (endpoint) => {
  return `${API_CONFIG.BASE_URL}${endpoint}`
} 