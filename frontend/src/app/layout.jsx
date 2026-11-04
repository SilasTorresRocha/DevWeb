export const metadata = {
  title: 'PlanoFácil - Sistema de Apoio ao Planejamento Docente',
  description: 'Sistema web para auxílio de professores da Educação Básica no planejamento de aulas alinhadas à BNCC.',
};

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <head>
        {/* Bootstrap 5 via CDN conforme apresentado em aula nos slides */}
        <link
          rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        />
      </head>
      <body className="bg-light">
        {children}
      </body>
    </html>
  );
}
