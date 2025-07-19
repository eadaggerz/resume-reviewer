const AnalysisResults = ({ data, onReset }) => {
  const { analysis, ai_feedback } = data

  const getMatchScoreColor = (score) => {
    if (score >= 80) return 'excellent'
    if (score >= 60) return 'good'
    if (score >= 40) return 'fair'
    return 'poor'
  }

  const getReadabilityLevel = (score) => {
    if (score >= 90) return 'Very Easy'
    if (score >= 80) return 'Easy'
    if (score >= 70) return 'Fairly Easy'
    if (score >= 60) return 'Standard'
    if (score >= 50) return 'Fairly Difficult'
    if (score >= 30) return 'Difficult'
    return 'Very Difficult'
  }

  return (
    <div className="analysis-results">
      <div className="results-header">
        <h2>📊 Analysis Results</h2>
        <button onClick={onReset} className="reset-btn">
          🔄 Analyze Another Resume
        </button>
      </div>

      {/* Match Score */}
      {analysis.job_keywords.length > 0 && (
        <div className="result-section">
          <h3>🎯 Job Match Score</h3>
          <div className={`match-score ${getMatchScoreColor(analysis.match_score)}`}>
            <span className="score-number">{analysis.match_score}%</span>
            <span className="score-label">Match</span>
          </div>
          
          {analysis.missing_keywords.length > 0 && (
            <div className="missing-keywords">
              <h4>Missing Keywords:</h4>
              <div className="keyword-tags">
                {analysis.missing_keywords.map((keyword, index) => (
                  <span key={index} className="keyword-tag missing">
                    {keyword}
                  </span>
                ))}
              </div>
            </div>
          )}
        </div>
      )}

      {/* Readability Analysis */}
      <div className="result-section">
        <h3>📖 Readability Analysis</h3>
        <div className="readability-metrics">
          <div className="metric">
            <span className="metric-label">Flesch Reading Ease:</span>
            <span className="metric-value">
              {analysis.readability.flesch_reading_ease?.toFixed(1) || 'N/A'}
            </span>
            <span className="metric-level">
              ({getReadabilityLevel(analysis.readability.flesch_reading_ease)})
            </span>
          </div>
          <div className="metric">
            <span className="metric-label">Grade Level:</span>
            <span className="metric-value">
              {analysis.readability.flesch_kincaid_grade?.toFixed(1) || 'N/A'}
            </span>
          </div>
          <div className="metric">
            <span className="metric-label">Word Count:</span>
            <span className="metric-value">
              {analysis.readability.lexicon_count || 'N/A'}
            </span>
          </div>
        </div>
      </div>

      {/* Grammar Issues */}
      {analysis.grammar_issues.length > 0 && (
        <div className="result-section">
          <h3>✏️ Grammar & Style Issues</h3>
          <div className="grammar-issues">
            {analysis.grammar_issues.map((issue, index) => (
              <div key={index} className="grammar-issue">
                ⚠️ {issue}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* AI Feedback */}
      {ai_feedback && (
        <div className="result-section">
          <h3>🤖 AI Feedback</h3>
          <div className="ai-feedback">
            <div className="feedback-content">
              {ai_feedback.general_feedback.split('\n').map((paragraph, index) => (
                <p key={index}>{paragraph}</p>
              ))}
            </div>
            
            {ai_feedback.suggested_rewrites && ai_feedback.suggested_rewrites.length > 0 && (
              <div className="suggested-rewrites">
                <h4>💡 Suggested Improvements:</h4>
                {ai_feedback.suggested_rewrites.map((suggestion, index) => (
                  <div key={index} className="rewrite-suggestion">
                    {suggestion}
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      )}

      {/* Resume Keywords */}
      <div className="result-section">
        <h3>🔑 Resume Keywords</h3>
        <div className="keyword-tags">
          {analysis.resume_keywords.map((keyword, index) => (
            <span key={index} className="keyword-tag">
              {keyword}
            </span>
          ))}
        </div>
      </div>
    </div>
  )
}

export default AnalysisResults 