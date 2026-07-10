import type { HTMLAttributes, ReactNode } from "react";
import { X } from "lucide-react";

type CardProps = HTMLAttributes<HTMLDivElement> & {
  children: ReactNode;
  title?: string;
  subtitle?: string;
  savedList?: boolean;
  onRemove?: () => void;
};

export default function Card({
  children,
  title,
  subtitle,
  className = "",
  savedList = false,
  onRemove,
  ...props
}: CardProps) {
  const isClickable = !!props.onClick;

  return (
    <div
      {...props}
      className={`
        relative
        rounded-2xl
        border border-gray-200
        bg-white
        p-6
        shadow-sm
        transition-all
        duration-200
        hover:shadow-md
        ${isClickable ? "cursor-pointer hover:-translate-y-1" : ""}
        ${className}
      `}
    >
      {savedList && (
        <button
          onClick={(e) => {
            e.stopPropagation();
            onRemove?.();
          }}
          className="absolute top-4 right-4 rounded-full p-1 text-gray-500 transition hover:bg-red-100 hover:text-red-600"
          aria-label="Remove Pokémon"
        >
          <X size={18} />
        </button>
      )}

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