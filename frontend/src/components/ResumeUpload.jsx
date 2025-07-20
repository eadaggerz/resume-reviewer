import { useState, useRef } from 'react'

const ResumeUpload = ({ onAnalysis, loading }) => {
  const [selectedFile, setSelectedFile] = useState(null)
  const [dragActive, setDragActive] = useState(false)
  const fileInputRef = useRef(null)

  const handleDrag = (e) => {
    e.preventDefault()
    e.stopPropagation()
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true)
    } else if (e.type === "dragleave") {
      setDragActive(false)
    }
  }

  const handleDrop = (e) => {
    e.preventDefault()
    e.stopPropagation()
    setDragActive(false)
    
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0])
    }
  }

  const handleFile = (file) => {
    if (file.type === 'application/pdf' || 
        file.type === 'application/vnd.openxmlformats-officedocument.wordprocessingml.document') {
      setSelectedFile(file)
    } else {
      alert('Please upload a PDF or DOCX file')
    }
  }

  const handleFileInput = (e) => {
    if (e.target.files && e.target.files[0]) {
      handleFile(e.target.files[0])
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    if (!selectedFile) {
      alert('Please select a resume file')
      return
    }

    const formData = new FormData()
    formData.append('resume', selectedFile)
    
    // Get job description from the form
    const jobDescription = document.getElementById('job-description')?.value || ''
    if (jobDescription) {
      formData.append('job_description', jobDescription)
    }

    onAnalysis(formData)
  }

  return (
    <div className="resume-upload">
      <h2>📄 Upload Your Resume</h2>
      
      <form onSubmit={handleSubmit}>
        <div 
          className={`upload-area ${dragActive ? 'drag-active' : ''}`}
          onDragEnter={handleDrag}
          onDragLeave={handleDrag}
          onDragOver={handleDrag}
          onDrop={handleDrop}
          onClick={() => fileInputRef.current?.click()}
        >
          <input
            ref={fileInputRef}
            type="file"
            accept=".pdf,.docx"
            onChange={handleFileInput}
            style={{ display: 'none' }}
          />
          
          {selectedFile ? (
            <div className="file-selected">
              <p>✅ {selectedFile.name}</p>
              <button 
                type="button" 
                onClick={(e) => {
                  e.stopPropagation()
                  setSelectedFile(null)
                }}
                className="remove-file"
              >
                Remove
              </button>
            </div>
          ) : (
            <div className="upload-prompt">
              <p>📁 Drag and drop your resume here</p>
              <p>or click to browse</p>
              <p className="file-types">Supports: PDF, DOCX</p>
            </div>
          )}
        </div>

        {loading ? (
          <div className="spinner-container" style={{ marginTop: '1rem' }}>
            <div className="spinner"></div>
          </div>
        ) : (
          <button 
            type="submit" 
            disabled={!selectedFile}
            className="analyze-btn"
          >
            🔍 Analyze Resume
          </button>
        )}
      </form>
    </div>
  )
}

export default ResumeUpload 