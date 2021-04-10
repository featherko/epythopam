"""Task 2."""
import sqlite3


class TableData:
    """Class to represent single table data from sqlite."""

    def __init__(self, database_name: str, table_name: str):
        self.table_name = table_name
        self.database_name = database_name

    def __len__(self) -> int:
        """Amount of rows in given table."""
        self._cursor.execute(f"select count(*) from {self.table_name}")
        return self._cursor.fetchone()[0]

    def __getitem__(self, item: str):
        """Get item protocol.

        Get us access to single data row for president with given name
        Example: presidents['Yeltsin'] # ('Yeltsin', 999, 'Russia')
        """
        self._cursor.execute(
            f"SELECT * from {self.table_name} where name=:name", {"name": item}
        )
        return self._cursor.fetchone()

    def __iter__(self):
        """Implement iter protocol.

        Let us iterate through the rows.
        """

        def dict_factory(row: tuple) -> dict:
            d = {}
            for idx, col in enumerate(self._cursor.description):
                d[col[0]] = row[idx]
            return d

        yield from (
            dict_factory(row)
            for row in self._cursor.execute(f"SELECT * from {self.table_name}")
        )

    def __contains__(self, item: str) -> bool:
        """Implement contains protocol.

        Checks if given item in the given table.
        """
        self._cursor.execute(f"SELECT * from {self.table_name}")
        return any(item in tab[0] for tab in self._cursor.fetchall())

    def __enter__(self):
        """Context manager enter."""
        self._conn = sqlite3.connect(self.database_name)
        self._cursor = self._conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # noqa: ANN001
        """Context manager exit."""
        self._conn.close()
