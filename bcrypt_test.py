from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "anderson1994"
hashed = pwd_context.hash(password)

print("HASH:", hashed)
print("¿Verifica correctamente?", pwd_context.verify(password, hashed))
