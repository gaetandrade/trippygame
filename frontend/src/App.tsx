import React from 'react';
import MainLayout from './components/layout/MainLayout';
import './App.css'; // Assuming create-react-app creates this, can be empty or removed if not needed

function App() {
  return (
    <MainLayout>
      {/* Content for the app will go here */}
      <div className="bg-white shadow-md rounded-lg p-6">
        <h2 className="text-2xl font-semibold text-gray-800 mb-4">Main Content Area</h2>
        <p className="text-gray-600">
          This is a placeholder for the application's main content.
          Future components and pages will be rendered within this layout.
        </p>
      </div>
    </MainLayout>
  );
}

export default App;
