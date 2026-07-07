import type { ReactNode } from "react";

type CardProps = {
  children: ReactNode;
  title?: string;
  subtitle?: string;
  className?: string;
  onClick?: () => void;
};

export default function Card({
  children,
  title,
  subtitle,
  className = "",
  onClick,
}: CardProps) {
  return (
    <div
      onClick={onClick}
      className={`
        rounded-2xl
        border border-gray-200
        bg-white
        p-6
        shadow-sm
        transition-all
        duration-200
        hover:shadow-md
        ${onClick ? "cursor-pointer hover:-translate-y-1" : ""}
        ${className}
      `}
    >
      {(title || subtitle) && (
        <div className="mb-4">
          {title && (
            <h2 className="text-xl font-semibold text-gray-900">
              {title}
            </h2>
          )}

          {subtitle && (
            <p className="mt-1 text-sm text-gray-500">
              {subtitle}
            </p>
          )}
        </div>
      )}

      {children}
    </div>
  );
}