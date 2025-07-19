const JobDescriptionForm = () => {
  return (
    <div className="job-description-form">
      <h3>💼 Job Description (Optional)</h3>
      <p className="form-description">
        Paste a job description to get personalized feedback and keyword matching
      </p>
      
      <textarea
        id="job-description"
        placeholder="Paste the job description here to get personalized feedback..."
        rows={6}
        className="job-description-textarea"
      />
      
      <div className="form-tips">
        <p>💡 Tips:</p>
        <ul>
          <li>Include key requirements and skills</li>
          <li>Add specific technologies or tools</li>
          <li>Include experience levels and qualifications</li>
        </ul>
      </div>
    </div>
  )
}

export default JobDescriptionForm 