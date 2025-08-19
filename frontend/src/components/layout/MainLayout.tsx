import React from 'react';

const MainLayout: React.FC<{ children?: React.ReactNode }> = ({ children }) => {
  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-blue-600 text-white p-4">
        <h1 className="text-xl">AI Content Platform</h1>
      </header>
      <main className="p-4">
        {children ? children : <p className="text-center text-gray-700">Welcome to the platform!</p>}
      </main>
      <footer className="bg-gray-800 text-white text-center p-4 mt-8">
        <p>&copy; $(date +%Y) AI Platform. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default MainLayout;
