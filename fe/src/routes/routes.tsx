// build the app routes

import { createBrowserRouter } from "react-router-dom";

import { ProtectedRoute } from "./ProtectedRoute";
import { Login } from "@/pages/auth/Login";
import { Register } from "@/pages/auth/Register";
import { Unauthorized } from "@/pages/auth/Unauthorized";
import { Home } from "@/pages/home/Home";

export const router = createBrowserRouter([
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/register",
    element: <Register />,
  },
  {
    path: "/unauthorized",
    element: <Unauthorized />,
  },
  {
    path: "/",
    element: (
      <ProtectedRoute roles={["super_admin"]}>
        <Home />
      </ProtectedRoute>
    ),
  },
]);
