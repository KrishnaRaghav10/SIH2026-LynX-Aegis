import React, { useEffect } from 'react';
import { useAegisStore } from '../store';
import { Role } from '../types';

interface RoleRouteGuardProps {
  requiredRole: Role;
  children: React.ReactNode;
}

export const RoleRouteGuard: React.FC<RoleRouteGuardProps> = ({ requiredRole, children }) => {
  const { currentUser, switchRole } = useAegisStore();

  useEffect(() => {
    if (currentUser.role !== requiredRole) {
      switchRole(requiredRole);
    }
  }, [currentUser.role, requiredRole, switchRole]);

  return <>{children}</>;
};
