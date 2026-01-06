export const Home = () => {
  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="px-8 py-6 mt-4 text-left bg-white shadow-lg">
        <h3 className="text-2xl font-bold text-center">Welcome to the Home Page!</h3>
        <p className="mt-4 text-center">This is a protected route for authenticated users.</p>
      </div>
    </div>
  );
};
