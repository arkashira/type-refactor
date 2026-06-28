# Tech Spec
## Stack
* Language: TypeScript
* Framework: Express.js
* Runtime: Node.js 18.x

## Hosting
* Primary Platform: GitHub Pages (free tier) for documentation and marketing site
* Backend Platform: AWS Lambda (free tier) for API and data processing
* Database Platform: MongoDB Atlas (free tier) for data storage

## Data Model
### Tables/Collections
#### RefactorHistory
* `_id` (ObjectId, primary key)
* `userId` (string, foreign key referencing Users collection)
* `refactorDate` (Date)
* `codeBefore` (string)
* `codeAfter` (string)
* `optimizationType` (string, e.g. "variable renaming", "function extraction")

#### Users
* `_id` (ObjectId, primary key)
* `username` (string)
* `email` (string)
* `passwordHash` (string)

### Key Fields
* `refactorHistory.userId` references `users._id`
* `users._id` is unique and indexed

## API Surface
### Endpoints
1. **POST /refactor**: Refactor code and return optimized version
	* Method: POST
	* Path: /refactor
	* Purpose: Refactor code and return optimized version
	* Request Body: `{ code: string, optimizationType: string }`
	* Response: `{ optimizedCode: string }`
2. **GET /refactor/history**: Get refactor history for a user
	* Method: GET
	* Path: /refactor/history
	* Purpose: Get refactor history for a user
	* Query Parameters: `userId: string`
	* Response: `[RefactorHistory]`
3. **POST /users**: Create a new user
	* Method: POST
	* Path: /users
	* Purpose: Create a new user
	* Request Body: `{ username: string, email: string, password: string }`
	* Response: `{ userId: string }`
4. **GET /users**: Get all users
	* Method: GET
	* Path: /users
	* Purpose: Get all users
	* Response: `[Users]`
5. **GET /health**: Get service health
	* Method: GET
	* Path: /health
	* Purpose: Get service health
	* Response: `{ status: string }`
6. **POST /refactor/validate**: Validate code and return errors
	* Method: POST
	* Path: /refactor/validate
	* Purpose: Validate code and return errors
	* Request Body: `{ code: string }`
	* Response: `[Error]`
7. **GET /refactor/stats**: Get refactor statistics
	* Method: GET
	* Path: /refactor/stats
	* Purpose: Get refactor statistics
	* Response: `{ refactorCount: number, optimizationCount: number }`
8. **POST /refactor/feedback**: Submit feedback on refactor
	* Method: POST
	* Path: /refactor/feedback
	* Purpose: Submit feedback on refactor
	* Request Body: `{ refactorId: string, feedback: string }`
	* Response: `{ feedbackId: string }`

## Security Model
* Authentication: JSON Web Tokens (JWT) with username and password
* Authorization: Role-Based Access Control (RBAC) with admin and user roles
* Secrets Management: AWS Secrets Manager for storing sensitive data
* IAM: AWS IAM for managing access to AWS resources

## Observability
* Logging: AWS CloudWatch Logs for logging API requests and errors
* Metrics: AWS CloudWatch Metrics for tracking API performance and usage
* Tracing: AWS X-Ray for tracing API requests and performance

## Build/CI
* Build Tool: GitHub Actions for building and deploying the application
* CI Pipeline: GitHub Actions for running automated tests and deploying the application
* Deployment: AWS Lambda and AWS API Gateway for deploying the application
* Testing: Jest and TypeScript for running automated tests and ensuring code quality