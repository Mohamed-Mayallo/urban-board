import { Navigate } from "react-router-dom";
import { useAuth } from "@/context/AuthContext";

export function ProtectedRoute({ children, roles }: any) {
  const { user, logout } = useAuth();

  if (!user) {
    logout();
    return <Navigate to="/login" />;
  }

  if (roles && !roles.includes(user.role)) {
    logout();
    return <Navigate to="/unauthorized" />;
  }

  return children;
}
