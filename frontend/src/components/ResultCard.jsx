function ResultCard({ answer, matched_skills, missing_skills, recommended_projects, confidence }) {
    return (
      <div className="bg-white rounded-xl shadow-sm border-l-4 border-emerald-500 p-6">
        <h2 className="text-lg font-semibold text-slate-700 mb-3">📊 AI 분석 결과</h2>
        <p className="text-slate-600 text-sm leading-relaxed whitespace-pre-line mb-4">{answer}</p>

        {confidence && (
          <div className="mt-4 pt-4 border-t border-gray-200">
            <h3 className="text-md font-semibold text-slate-700 mb-2">신뢰도</h3>
            <div className="w-full bg-gray-200 rounded-full h-2.5">
              <div className="bg-emerald-600 h-2.5 rounded-full" style={{ width: `${confidence}%` }}></div>
            </div>
            <p className="text-right text-sm text-slate-500 mt-1">{confidence}%</p>
          </div>
        )}

        {matched_skills && matched_skills.length > 0 && (
          <div className="mt-4 pt-4 border-t border-gray-200">
            <h3 className="text-md font-semibold text-slate-700 mb-2">매칭된 스킬</h3>
            <div className="flex flex-wrap gap-2">
              {matched_skills.map((skill, index) => (
                <span key={index} className="bg-emerald-100 text-emerald-800 text-xs font-medium px-2.5 py-0.5 rounded-full">
                  {skill}
                </span>
              ))}
            </div>
          </div>
        )}

        {missing_skills && missing_skills.length > 0 && (
          <div className="mt-4 pt-4 border-t border-gray-200">
            <h3 className="text-md font-semibold text-slate-700 mb-2">부족한 스킬</h3>
            <div className="flex flex-wrap gap-2">
              {missing_skills.map((skill, index) => (
                <span key={index} className="bg-red-100 text-red-800 text-xs font-medium px-2.5 py-0.5 rounded-full">
                  {skill}
                </span>
              ))}
            </div>
          </div>
        )}

        {recommended_projects && recommended_projects.length > 0 && (
          <div className="mt-4 pt-4 border-t border-gray-200">
            <h3 className="text-md font-semibold text-slate-700 mb-2">추천 프로젝트</h3>
            <ul className="list-disc list-inside text-slate-600 text-sm space-y-1">
              {recommended_projects.map((project, index) => (
                <li key={index}>{project}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    );
  }
  export default ResultCard;