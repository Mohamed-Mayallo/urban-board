import { createContext, useContext, useState } from "react";
import { jwtDecode } from "jwt-decode";
import { api } from "@/lib/api";

type User = {
  role: string;
};

const AuthContext = createContext<any>(null);

export function AuthProvider({ children }: any) {
  const userFromLocalStorage = localStorage.getItem("user");
  const savedUser = userFromLocalStorage ? JSON.parse(userFromLocalStorage) : null;

  const [user, setUser] = useState<User | null>(savedUser);

  const login = async (email: string, password: string) => {
    const tokenRes = await api.post("/auth/login/", { email, password });
    const token = tokenRes.data.access;

    if (!token) {
      throw new Error("Authentication failed. Please try again.");
    }

    const userRes = await api.get("/auth/me/", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    const user = userRes.data;

    if (!user) {
      throw new Error("User information not found");
    }

    const decodedToken = jwtDecode(token);
    const isExpired = decodedToken.exp! * 1000 < Date.now();

    if (isExpired) {
      throw new Error("Token has expired");
    }

    localStorage.setItem("user", JSON.stringify(user));
    setUser(user);
  };

  const logout = () => {
    localStorage.clear();
    setUser(null);
  };

  return <AuthContext.Provider value={{ user, login, logout }}>{children}</AuthContext.Provider>;
}

export const useAuth = () => useContext(AuthContext);
