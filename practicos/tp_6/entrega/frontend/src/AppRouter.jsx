import { createHashRouter, RouterProvider } from "react-router-dom";
import LandingPage from "./componentes/LandingPage";
import TicketsForm from "./componentes/ticketsForm";
import QrView from "./componentes/qrView";

// 1. Definimos las rutas usando la nueva API de objetos
const router = createHashRouter([
  {
    path: "/",
    element: <LandingPage />,
  },
  {
    path: "/buy",
    element: <TicketsForm />,
  },
  {
    path: "/qrView",
    element: <QrView />,
  },
]);

// 2. Exportamos el proveedor que usará esa configuración
export const AppRouter = () => {
  return <RouterProvider router={router} />;
};
