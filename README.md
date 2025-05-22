# Assignment Reminder and Tracking App

A comprehensive cross-platform application (Web, iOS, Android) designed to help students, tutors, and administrators manage assignments, notifications, and academic registrations efficiently.

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [User Roles](#user-roles)
- [API Documentation](#api-documentation)
- [Security Features](#security-features)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Core Functionality

- **Assignment Management**: Create, edit, delete, and track assignments
- **Real-time Notifications**: Push notifications on mobile, instant updates on web
- **Support Ticket System**: Text-based communication with file attachments
- **User Management**: Multi-role system with different permission levels
- **Performance Tracking**: Message receipts and response time monitoring
- **Offline Support**: Work offline on mobile, sync when connected

### Mobile-Specific Features

- Push Notifications (FCM for Android, APNs for iOS)
- Biometric Authentication (Face ID/Touch ID)
- Camera Integration for document scanning
- Native File Picker
- Background Sync
- App Shortcuts (3D Touch/App Shortcuts)

### Advanced Features

- Two-Factor Authentication (2FA)
- Session Management with auto-logout
- Activity Logging and Audit Trail
- 48-hour Conversation Retention Policy
- Mobile-Responsive Design
- File Upload Support

## 🛠 Technology Stack

### Backend (Shared API)

- **API**: Node.js with Express.js
- **Database**: PostgreSQL
- **Authentication**: JWT with refresh tokens
- **Real-time**: Socket.io
- **Cache**: Redis
- **File Storage**: AWS S3 / Local Storage
- **Database ORM**: Sequelize (Node.js) / SQLAlchemy (Python scripts)

### Frontend Options

#### Option 1: React Native (Recommended)

- **Web**: React.js
- **Mobile**: React Native (iOS & Android)
- **Shared Logic**: 70-80% code reuse
- **UI Framework**: React Native Web for maximum code sharing

#### Option 2: Separate Native Apps

- **Web**: React.js
- **iOS**: Swift/SwiftUI
- **Android**: Kotlin/Jetpack Compose

#### Option 3: Progressive Web App (PWA)

- **Framework**: React.js with PWA features
- **Mobile**: Installable PWA
- **Offline**: Service Workers

## 📁 Project Structure

```
assignment-tracker/
├── apps/                        # Frontend applications
│   ├── web/                     # Web application (React)
│   │   ├── public/
│   │   ├── src/
│   │   └── package.json
│   │
│   └── mobile/                  # Mobile application (React Native)
│       ├── android/             # Android-specific code
│       ├── ios/                 # iOS-specific code
│       ├── src/
│       │   ├── components/      # Mobile components
│       │   ├── screens/         # Mobile screens
│       │   ├── navigation/      # Navigation setup
│       │   └── services/        # API services
│       └── package.json
│
├── packages/                    # Shared packages
│   ├── shared/                  # Shared business logic
│   │   ├── constants/          # Shared constants
│   │   ├── types/              # TypeScript types
│   │   ├── utils/              # Shared utilities
│   │   └── validators/         # Shared validation
│   │
│   └── ui/                     # Shared UI components
│       ├── components/         # Cross-platform components
│       └── themes/             # Shared theme system
│
├── server/                      # Backend application
│   ├── src/
│   │   ├── config/             # Configuration files
│   │   ├── controllers/        # Request handlers
│   │   ├── middleware/         # Custom middleware
│   │   ├── models/             # Database models
│   │   ├── routes/             # API routes
│   │   ├── services/           # Business logic
│   │   ├── utils/              # Utility functions
│   │   ├── validators/         # Input validation
│   │   └── app.js              # Express app setup
│   ├── tests/                  # Test files
│   └── package.json
│
├── database/                    # Database scripts
│   ├── migrations/             # Database migrations
│   ├── seeds/                  # Seed data
│   └── init.py                 # Python initialization script
│
├── docs/                       # Documentation
│   ├── API.md                  # API documentation
│   ├── DEPLOYMENT.md           # Deployment guide
│   ├── MOBILE.md              # Mobile development guide
│   └── SECURITY.md             # Security guidelines
│
├── docker/                     # Docker configuration
│   ├── Dockerfile.web
│   ├── Dockerfile.mobile
│   ├── Dockerfile.server
│   └── docker-compose.yml
│
├── scripts/                    # Utility scripts
│   ├── setup.sh               # Initial setup script
│   └── backup.sh              # Database backup script
│
├── .env.example               # Environment variables template
├── .gitignore
├── LICENSE
├── package.json               # Root package.json for monorepo
└── README.md
```

## 🚀 Installation

### Prerequisites

- Node.js (v16 or higher)
- PostgreSQL (v13 or higher)
- Redis (v6 or higher)
- Python 3.8+ (for database scripts)
- npm or yarn
- **For Mobile Development:**
  - React Native CLI
  - Android Studio (for Android)
  - Xcode (for iOS, macOS only)
  - CocoaPods (iOS)

### Setup Instructions

#### 1. Clone the repository

```bash
git clone https://github.com/yourusername/assignment-tracker.git
cd assignment-tracker
```

#### 2. Install dependencies

```bash
# Install root dependencies (for monorepo management)
npm install

# Install server dependencies
cd server
npm install

# Install web dependencies
cd ../apps/web
npm install

# Install mobile dependencies
cd ../mobile
npm install

# iOS specific (macOS only)
cd ios
pod install
```

#### 3. Set up environment variables

```bash
# Copy the example env file
cp .env.example .env

# Edit .env with your configuration
```

#### 4. Initialize the database

```bash
# Run Python script for database setup
cd database
python init.py

# Run migrations
cd ../server
npm run migrate
```

#### 5. Start the application

```bash
# Start Redis
redis-server

# Start backend (from server directory)
npm run dev

# Start web app (from apps/web directory)
npm start

# Start mobile app
# For iOS (from apps/mobile directory)
npm run ios

# For Android
npm run android
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Server Configuration
NODE_ENV=development
PORT=5000
CLIENT_URL=http://localhost:3000

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=assignment_tracker
DB_USER=your_db_user
DB_PASSWORD=your_db_password

# Authentication
JWT_SECRET=your_jwt_secret_key
JWT_REFRESH_SECRET=your_jwt_refresh_secret
JWT_EXPIRE=15m
JWT_REFRESH_EXPIRE=7d

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=

# 2FA Configuration
TWO_FACTOR_APP_NAME=AssignmentTracker
TWO_FACTOR_ISSUER=YourCollege

# File Upload
MAX_FILE_SIZE=10485760  # 10MB in bytes
ALLOWED_FILE_TYPES=pdf,doc,docx,txt,jpg,png

# Session Configuration
SESSION_TIMEOUT=1800000  # 30 minutes in milliseconds

# Email Configuration (optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password

# Push Notifications
FCM_SERVER_KEY=your_firebase_server_key
APNS_KEY_ID=your_apple_key_id
APNS_TEAM_ID=your_apple_team_id

# Mobile App Configuration
APP_SCHEME=assignmenttracker
DEEP_LINK_PREFIX=https://app.yourcollege.edu
```

## 👥 User Roles

### 1. Admin

- Full system control and configuration
- User role and access management
- System performance monitoring
- Generate system-wide reports

### 2. Administration (Secretary)

- Create and manage user accounts
- Handle user registrations
- Update user profiles
- Manage course and department information

### 3. Tutors

- Create and assign homework
- Set assignment deadlines
- Upload course materials
- Track student submissions
- Open support tickets
- Manage student communications

### 4. Students

- View personalized notifications
- Access current assignments
- Submit assignments
- Communicate through support tickets
- Track submission status

## 📚 API Documentation

### Authentication Endpoints

- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `POST /api/auth/refresh` - Refresh JWT token
- `POST /api/auth/2fa/enable` - Enable 2FA
- `POST /api/auth/2fa/verify` - Verify 2FA code

### User Management

- `GET /api/users` - List all users (Admin only)
- `POST /api/users` - Create new user
- `GET /api/users/:id` - Get user details
- `PUT /api/users/:id` - Update user
- `DELETE /api/users/:id` - Delete user

### Assignment Management

- `GET /api/assignments` - List assignments
- `POST /api/assignments` - Create assignment
- `GET /api/assignments/:id` - Get assignment details
- `PUT /api/assignments/:id` - Update assignment
- `DELETE /api/assignments/:id` - Delete assignment

### Support Tickets

- `GET /api/tickets` - List tickets
- `POST /api/tickets` - Create ticket
- `GET /api/tickets/:id` - Get ticket details
- `POST /api/tickets/:id/messages` - Add message to ticket
- `POST /api/tickets/:id/close` - Close ticket

### Notifications

- `GET /api/notifications` - Get user notifications
- `POST /api/notifications/register` - Register device for push notifications
- `PUT /api/notifications/:id/read` - Mark notification as read
- `DELETE /api/notifications/device/:token` - Unregister device

For detailed API documentation, see [docs/API.md](docs/API.md)

## 🔒 Security Features

### Authentication & Authorization

- JWT-based authentication with refresh tokens
- Role-based access control (RBAC)
- Two-factor authentication support

### Password Security

- Minimum 12 characters
- Requires uppercase, lowercase, numbers, and symbols
- Password strength validation
- Bcrypt hashing with salt rounds

### Session Management

- Secure session handling
- Automatic logout on inactivity
- Device tracking
- Remote session termination

### Activity Logging

- Comprehensive audit trail
- Login/logout tracking
- Critical action logging
- Tamper-evident log storage

### Data Protection

- HTTPS enforcement
- Input validation and sanitization
- SQL injection prevention
- XSS protection
- CSRF protection

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow ESLint configuration
- Write unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support, email support@yourcollege.edu or open an issue in the GitHub repository.

## 🔮 Future Enhancements

- [ ] Email notifications
- [ ] Calendar integration
- [ ] Grade tracking
- [ ] Attendance management with geolocation
- [ ] Offline mode for full app functionality
- [ ] Voice notes for assignments
- [ ] Video conferencing integration
- [ ] Bulk assignment upload
- [ ] Analytics dashboard
- [ ] Integration with college LMS
- [ ] Wearable device support (Apple Watch, WearOS)
- [ ] Desktop applications (Electron)

## 📱 Mobile Development Resources

- [React Native Documentation](https://reactnative.dev/)
- [Expo Documentation](https://docs.expo.dev/) (if using Expo)
- [Mobile Development Guide](docs/MOBILE.md)
