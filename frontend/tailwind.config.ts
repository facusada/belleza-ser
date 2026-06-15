import type { Config } from 'tailwindcss'

export default {
  content: [
    './components/**/*.{vue,js,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './app.vue',
    './data/**/*.ts',
    './composables/**/*.ts'
  ],
  theme: {
    extend: {
      colors: {
        // Paleta cálida / espiritual: tierra · lavanda · dorado · crema.
        bs: {
          cream: '#FBF6EF',
          sand: '#F0E4D6',
          clay: '#C9A18A',
          gold: '#C9A24B',
          lavender: '#B7A4D4',
          plum: '#6B5A86',
          ink: '#403A36',
          muted: '#8A7E72'
        }
      },
      fontFamily: {
        display: ['"Cormorant Garamond"', 'Georgia', 'serif'],
        body: ['"Nunito Sans"', 'system-ui', 'sans-serif']
      },
      boxShadow: {
        soft: '0 18px 50px rgba(64, 58, 54, 0.10)',
        card: '0 12px 30px rgba(107, 90, 134, 0.10)'
      },
      backgroundImage: {
        'bs-aura':
          'radial-gradient(circle at 78% 22%, rgba(183,164,212,.28), transparent 42%), radial-gradient(circle at 14% 80%, rgba(201,162,75,.16), transparent 40%)'
      },
      keyframes: {
        'fade-up': {
          '0%': { opacity: '0', transform: 'translateY(24px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' }
        }
      },
      animation: {
        'fade-up': 'fade-up .7s ease-out forwards'
      }
    }
  },
  plugins: []
} satisfies Config
