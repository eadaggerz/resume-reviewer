import { useState } from 'react'
import './App.css'
import ResumeUpload from './components/ResumeUpload'
import JobDescriptionForm from './components/JobDescriptionForm'
import AnalysisResults from './components/AnalysisResults'
import { getApiUrl, API_CONFIG } from './config'

function App() {
  const [analysisData, setAnalysisData] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleAnalysis = async (formData) => {
    setLoading(true)
    setError(null)
    
    try {
      const response = await fetch(getApiUrl(API_CONFIG.ENDPOINTS.ANALYZE_RESUME), {
        method: 'POST',
        body: formData,
      })
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const data = await response.json()
      setAnalysisData(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="App">
      <header className="app-header">
        <a href="/"><h1>🤖 AI Resume Reviewer</h1></a>
        <p>Upload your resume and get AI-powered feedback</p>
      </header>

      <main className="app-main">
        {!analysisData ? (
          <div className="upload-section">
            <ResumeUpload onAnalysis={handleAnalysis} loading={loading} />
            <JobDescriptionForm />
          </div>
        ) : (
          <AnalysisResults 
            data={analysisData} 
            onReset={() => setAnalysisData(null)}
          />
        )}
        
        {error && (
          <div className="error-message">
            <p>❌ Error: {error}</p>
          </div>
        )}
      </main>
    </div>
  )
}

export default App
