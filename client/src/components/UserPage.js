import { useEffect, useState } from "react";


function UserPage() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("/users")
    .then((r) => r.json())
    .then((usersArray) => {
      setUsers(usersArray);
    });
  }, [])

    return (
      <ul>
        {users.map((u) => {
          return <h1>{u.greeting}</h1>;
        })}
      </ul>
    )
  }
  
export default UserPage;